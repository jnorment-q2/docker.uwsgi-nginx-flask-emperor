
mkdir -p ignore

echo "
[agent]
app = some-app
tier = some-tier
node = some-node

[controller]
host = ???
port = 443
ssl = True
account = ???
accesskey = ??? 
" > ignore/appd.ini

echo 'Update contents of ./ignore/appd.ini with Q2 configuration: vim ignore/appd.ini'
