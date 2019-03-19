#!/bin/bash

lazygit() {
    git add .
    git commit -a -m "Automated Nightly Git Push"
    git push origin master
}

lazygit

