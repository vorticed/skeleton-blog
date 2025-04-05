set -e
sudo mkdir -p /home/$SERVER_USER/$DEPLOY_DIR/nginx
sudo cp -r /home/$SERVER_USER/tmp/$DOMAIN/nginx/* /home/$SERVER_USER/$DEPLOY_DIR/nginx
sudo chown -R $SERVER_USER:$SERVER_USER /home/$SERVER_USER/$DEPLOY_DIR/nginx
if [ ! -f "/etc/nginx/conf.d/nic/${DOMAIN}.conf" ]; then
  sudo cp /home/$SERVER_USER/${DEPLOY_DIR}/nginx/nic.conf /etc/nginx/conf.d/nic/${DOMAIN}.conf
fi
sudo certbot --nginx -d "$DOMAIN" --non-interactive --agree-tos -m "$CERTBOT_EMAIL"
sudo systemctl reload nginx
