# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
	
	config.vm.define :dev_agnt_srvr do |dev_agnt_srvr|
	    dev_agnt_srvr.vm.box = "ubuntu/trusty64"
	    dev_agnt_srvr.vm.network "private_network", ip: "192.168.60.102"
	    dev_agnt_srvr.vm.hostname = "dev-agnt-srvr.tiwaz.cloud"
	
	    dev_agnt_srvr.vm.synced_folder ".", "/vagrant", id: "vagrant-root",
	        owner: "vagrant",
	        group: "vagrant",
	        mount_options: ["dmode=775,fmode=664"]
	    
	    dev_agnt_srvr.vm.provider :virtualbox do |vb|
			vb.name = "vagrant-agnt-srvr.tiwaz.cloud"
	        vb.customize ["modifyvm", :id, "--name", "dev-agnt-srvr.tiwaz.cloud", "--memory", "2048"]
	        # Uncomment for Windows install
	        #vb.customize ["setextradata", :id, "VBoxInteral2/SharedFoldersEnableSymlinksCreate/v-root", "1"]
	    end
	
	    dev_agnt_srvr.vm.provision :shell, path: "devops/dev-agnt-srvr-bootstrap.sh"
	 	#dev_agnt_srvr.disksize.size = '25GB'
	end
		
		
end
