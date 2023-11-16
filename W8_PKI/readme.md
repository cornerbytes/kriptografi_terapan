## create folder
mkdir certs
mkdir private
mkdir db

touch db/index
echo 1000 > db/serial
echo 1000 > db/crlnumber

## create root CA 
`openssl req -x509 -config ca.conf -extensions ca_ext -newkey rsa:4096 -keyout private/root-ca.key -out certs/root-ca.crt -days 1825`

## create intermediate csr and pair key
`openssl req -config ca.conf -extensions sub_ca_ext -newkey rsa:4096 -keyout private/intermediate-ca.key -out certs/intermediate-ca.csr`

## create sign the intermediate csr using certificate root
`openssl ca -config ca.conf -extensions sub_ca_ext -in certs/intermediate-ca.csr -out certs/intermediate-ca.crt -days 1095`

