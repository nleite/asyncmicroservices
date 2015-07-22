#!/bin/sh

boot2dockervm=boot2docker-vm
VBoxManage modifyvm "$boot2dockervm" --natpf1 "tcp-port35000,tcp,,35000,,35000"
