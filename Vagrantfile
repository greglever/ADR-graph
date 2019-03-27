Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/bionic64"

  config.vm.provision "shell", inline: <<-SHELL
    add-apt-repository ppa:igraph/ppa
    apt-get update
    apt-get install r-base-core  
    apt-get install python-igraph
    pip install rpy2==2.7.4
    pip install numpy scipy
  SHELL
end

