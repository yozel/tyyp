import requests
from scapy.all import sr1, IP, UDP, DNS, DNSQR
from urllib.parse import urlparse

DNS_SERVERS = {
    "ISP": {
        "TR": {
            "TURKTELEKOM": {
                'legacy': ['195.175.39.49', '195.175.39.50'],
            },
            "KABLONET": {
                'legacy': ['62.248.80.161', '62.248.80.162'],
            }
        }
    },
    "GOOGLE": {
        'legacy': ['8.8.8.8', '8.8.4.4'],
    },
    "CLOUDFLARE": {
        'legacy': ['1.1.1.1', '1.0.0.1'],
        'doh': ['cloudflare-dns.com'],
    },
}


class DNSChecker(object):
    def startup(self):
        try:
            # https://www.iana.org/assignments/dns-parameters/dns-parameters.xhtml#dns-parameters-6
            cloudflare_doh_server = DNS_SERVERS['CLOUDFLARE']['doh'][0]
            doh_response = self._doh_request('cloudflare-dns.com', dns_server=cloudflare_doh_server)
            assert doh_response['Status'] == 0, "Status(RCODE) is not 0"
        except Exception as e:
            print("There is a problem with DoH")
            raise e

    def check(self, url):
	domain = urlparse(url).hostname
        country = "TR"
        doh_r = self._doh_request(domain, dns_server=DNS_SERVERS['CLOUDFLARE']['doh'][0])
        assert doh_r['Status'] == 0, "Site does not exist"

        results = {}
        for isp, dns_servers in DNS_SERVERS['ISP'][country].items():
            for dns_server in dns_servers['legacy']:
                try:
                    dns_r = self._dns_request(domain, dns_server=dns_server)
                    msg = "Ok" if dns_r.rcode == 0 else "Failed"
                    # TODO: Handle wrong responses too
                    results[(isp, dns_server)] = dns_r
                except TimeoutError:
                    msg = "Timeout"
                print(domain, isp, dns_server, msg)

    @staticmethod
    def _doh_request(q_name, dns_server=DNS_SERVERS['CLOUDFLARE']['doh'][0], q_type='A'):
        return requests.get(
            "https://%s/dns-query?name=%s&type=%s" % (dns_server, q_name, q_type),
            headers={'accept': 'application/dns-json'}).json()

    @staticmethod
    def _dns_request(q_name, dns_server):
        result = sr1(IP(dst=dns_server) / UDP(dport=53) / DNS(rd=1, qd=DNSQR(qname=q_name)), verbose=0, timeout=10)
        if result:
            return result[DNS]
        else:
            raise TimeoutError()
