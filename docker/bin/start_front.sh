#!/bin/bash
cd /app/frontend
npm run build
pm2 start node_modules/nuxt/bin/nuxt-start -i 2 --name=nuxt -l /tmp/nuxt.log
pm2 logs
