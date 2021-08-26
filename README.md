# ansible-test
The following command is needed to be able to run vagrant up:
vagrant plugin install vagrant-libvirt

For the playbook to run on provisioning: 

 * Encrypt password for add user/permissions with: 
python -c "from passlib.hash import sha512_crypt; import getpass; print(sha512_crypt.using(rounds=5000).hash(getpass.getpass()))"

 * Replace username/password for configure subscriptions

