#!/bin/bash
set -e

if [ -d /home/$SERVER_USER/$DEPLOY_DIR/html ]; then
  sudo rm -r /home/$SERVER_USER/$DEPLOY_DIR/html
fi
sudo mkdir -p /home/$SERVER_USER/$DEPLOY_DIR/html
sudo cp -r /home/$SERVER_USER/tmp/$DOMAIN/html/* /home/$SERVER_USER/$DEPLOY_DIR/html
sudo chown -R $SERVER_USER:$SERVER_USER /home/$SERVER_USER/$DEPLOY_DIR/html
sudo find /home/$SERVER_USER/$DEPLOY_DIR/html -type d -exec chmod 755 {} \;
sudo find /home/$SERVER_USER/$DEPLOY_DIR/html -type f -exec chmod 644 {} \;
