Disclaimer:

This tool is intended solely for educational purposes and project work. The developer assumes no responsibility for any misuse of this script.

It is strongly advised that users understand the ethical and legal implications of using penetration testing tools. The most effective method for security assessment is manual testing. This script is designed to provide a list of potential exploits, which should then be manually verified and further investigated on systems you have explicit permission to test.

Under no circumstances should this script be used to test or exploit websites or systems without the express consent of the owner. If you are testing this code, please use demo WordPress websites specifically set up for security testing, and not real or production environments.

By using this script, you acknowledge and agree to these terms and conditions. Any actions taken using this tool are your sole responsibility.

Important Note for Option 2: Please be aware that due to redirects implemented by either Google or the target WordPress site, this option may sometimes generate false positive results. Always manually verify the findings to ensure accuracy.

**Nebula Strike Usage Guide:**

Nebula Strike is a Python-based penetration testing tool for WordPress websites, offering features like brute-forcing, registration exploitation, subdomain gathering, and SQL injection detection.

Here's how to use some of its key features:

**2. Bruteforce based on file (Sites and Credentials):**

To perform a brute-force attack using a file containing site URLs and credentials, follow this format for your input text file:

```
https://www.example.com/wp-login.php#username@password
https://another-site.com/login#admin@pass123
https://target-wordpress.net/wp/login.php#testuser@securepass
# ... more entries in the same format
```

* **Format:** `[WordPress Login URL]#[Username]@[Password]`
* Create a text file adhering to this format, with each site and credential pair on a new line.
* Provide this text file as input to Nebula Strike's brute-force option.

**3. Dark Portal - WP Register Exploiter Usage:**

To use the registration exploitation feature:

* Create a text file containing the base URLs of the WordPress sites you want to target.
* **Example Text File Content:**
    ```
    https://www.evil.com/
    https://another-vulnerable-site.org/
    # ... more base URLs
    ```
* **Important:** Ensure the URLs point to the base domain of a WordPress site.
* Input this text file into the "Dark Portal" module of Nebula Strike.

**4. SQL Injection Detector Usage:**

To utilize the SQL injection detection feature:

* Create a text file containing target URLs with parameters that you suspect might be vulnerable to SQL injection.
* **Example Text File Content:**
    ```
    https://www.evil.com/page.php?id=12
    https://vulnerable-site.net/article.php?category=news&item=45
    https://test-site.org/index.php?product_id=abc
    # ... more URLs with parameters
    ```
* **Format:** Include the full URL with the parameters you want to test.
* Provide this text file as input to the SQL injection detector tool within Nebula Strike.
* The tool will analyze these URLs and identify potentially vulnerable websites, marking SQL injection errors.
* The results, including identified vulnerable websites, will be saved in an output file.
