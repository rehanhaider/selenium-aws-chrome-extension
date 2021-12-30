echo "Getting Chrome version..."
chrome_version=($(google-chrome-stable --version))
version=${chrome_version[2]}
chrome_version=${version%.*}
echo "Chrome version: ${chrome_version}"

echo "Getting latest chromedriver version"
chromedriver_version_full=$(curl "https://chromedriver.storage.googleapis.com/LATEST_RELEASE")
version=${chromedriver_version_full}
chromedriver_version=${version%.*}
echo "Chromedriver version: ${chromedriver_version}"

if [ "${chrome_version}" == "$chromedriver_version" ]; then
    echo "Compatible Chromedriver is available..."
    echo "Proceeding with installation..."
else
    echo "Compabible Chromedriver not available...exiting"
    exit 1
fi

echo "Downloading latest Chromedriver..."
mkdir -p "/opt/chromedriver/stable/"

 curl 'https://www.googleapis.com/download/storage/v1/b/chromium-browser-snapshots/o/Linux_x64%2F954502%2Fchromedriver_linux64.zip?generation=1640815530134396&alt=media' \
  -H 'authority: www.googleapis.com' \
  -H 'sec-ch-ua: " Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Windows"' \
  -H 'dnt: 1' \
  -H 'upgrade-insecure-requests: 1' \
  -H 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36' \
  -H 'accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9' \
  -H 'x-client-data: CLO1yQEIhrbJAQiktskBCMG2yQEIqZ3KAQjRoMoBCMCXywEI6vLLAQie+csBCNf8ywEI5oTMAQi1hcwBCMuJzAEI0IvMAQisjswBCJqPzAEI0o/MAQjakMwBCMmSzAEIoZPMAQjHk8wBCIqUzAEY5KDLAQ==' \
  -H 'sec-fetch-site: none' \
  -H 'sec-fetch-mode: navigate' \
  -H 'sec-fetch-user: ?1' \
  -H 'sec-fetch-dest: document' \
  -H 'accept-language: en-GB,en-US;q=0.9,en;q=0.8,ms;q=0.7' \
  --compressed > /opt/chromedriver/stable/chromedriver_linux64.zip



unzip -q "/opt/chromedriver/stable/chromedriver_linux64.zip" \
    -d "/opt/chromedriver/stable/"

mv /opt/chromedriver/stable/chromedriver_linux64/chromedriver /opt/chromedriver/stable/chromedriver

chmod +x "/opt/chromedriver/stable/chromedriver"
rm -rf "/opt/chromedriver/stable/chromedriver_linux64.zip"

echo "Chrome & Chromedriver installed"