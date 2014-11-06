#!/bin/sh
# Generated self-signed certificate SSL for web-server use that script.
#
# For generate personal key on client side example:
#
# ssh-keygen -b 1024 -t dsa -N passphrase -f mykey -C "ignat99@gmail.com"
# cat mykey.pub > ~/.ssh/authorized_keys
# chmod 0600 ~/.ssh/authorized_keys


set -e
tmpdir="/tmp"
certdir="/etc/lighttpd"
if [ -f $certdir/server.pem ] ; then
echo "certificate already exists."
echo "To recreate the certificate, delete the file $certdir/server.pem"
exit 0
fi
#generate https certificate
cat > $tmpdir/cert.cnf << "EOF"
RANDFILE = /dev/urandom
[ req ]
default_bits = 1024
encrypt_key = yes
distinguished_name = req_dn
x509_extensions = cert_type
prompt = no
[ req_dn ]
C=ES
ST=ESPAIN
L=Madrid
O=Msp
OU=Msp
CN=msp.tk
emailAddress=none@msp.tk

[ cert_type ]
basicConstraints	= critical,CA:FALSE
nsCertType		= server
nsComment		= "MSP SSL Certificate"
subjectKeyIdentifier	= hash
authorityKeyIdentifier	= keyid,issuer:always
issuerAltName		= issuer:copy
keyUsage		= keyEncipherment, digitalSignature
extendedKeyUsage	= serverAuth
EOF

openssl req -new -outform PEM -config $tmpdir/cert.cnf -out $tmpdir/server.pem -newkey rsa:2048 -nodes -keyout $tmpdir/server.key -keyform PEM -days 9999 -x509
cat $tmpdir/server.pem $tmpdir/server.key > $certdir/server.pem
rm -f $tmpdir/cert.cnf $tmpdir/server.pem $tmpdir/server.key
echo "Successfully generated self-signed certificate"

