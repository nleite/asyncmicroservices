#!/bin/sh

boot2dockervm=boot2docker-vm
port=35000
VBoxManage modifyvm "$boot2dockervm" --natpf1 delete "tcp-port$port"
