## download zip and unzip
`unzip W8_PKI.zip -d automate`

`cd automate`

## modify default section in ca.conf and personal-ca.conf

pastikan modif ini sesuai kelompok masing masing

[default]

SAN = DNS:pbl-rks304.local,DNS:*.pbl-rks304.local 

name = root-ca

url = pbl-rks304.local


## create folder
 - `mkdir certs`
 - `mkdir private`
 - `mkdir db`
 - `touch db/index`
 - `echo 1000 > db/serial`
 - `echo 1000 > db/crlnumber`


## create root CA 
`openssl req -x509 -config ca.conf -extensions ca_ext -newkey rsa:4096 -keyout private/root-ca.key -out certs/root-ca.crt -days 1825`

pastikan O dan CN sesuai dengan ketentuan tugas

## create intermediate csr and pair key
`openssl req -config ca.conf -extensions sub_ca_ext -newkey rsa:4096 -keyout private/intermediate-ca.key -out certs/intermediate-ca.csr`

pastikan O dan CN sesuai dengan ketentuan tugas

## create sign the intermediate csr using certificate root
`openssl ca -config ca.conf -extensions sub_ca_ext -in certs/intermediate-ca.csr -out certs/intermediate-ca.crt -days 1095`

## run the tool for automate the user 
 - `chmod +x all_tool`
 - `./all_tool`
 - enter email and name

done!


## install file .pf12
 - install .pf12 di laptop masing masing

## outlook setting

see this 
 - https://www.thesslstore.com/knowledgebase/email-signing-support/install-e-mail-signing-certificates-outlook/

## tips
 - baca ketika tool atau promptnya error kenapa
 - pastikan isi password sesuai antara root-ca intermediate-ca ataupun apapun itu (baca baik-baik)


