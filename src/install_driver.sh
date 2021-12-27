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
curl -Lo "/opt/chromedriver/stable/chromedriver_linux64.zip" \
    "https://chromedriver.storage.googleapis.com/$chromedriver_version_full/chromedriver_linux64.zip"

unzip -q "/opt/chromedriver/stable/chromedriver_linux64.zip" \
    -d "/opt/chromedriver/stable/"

chmod +x "/opt/chromedriver/stable/chromedriver"
rm -rf "/opt/chromedriver/stable/chromedriver_linux64.zip"

echo "Chrome & Chromedriver installed"