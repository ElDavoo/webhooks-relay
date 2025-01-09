# webhooks-relay
Catches all HTTP requests to /webhooks/<name> and forwards them to  
the container <name>. Made to be used in a Docker Compose network.  
Made to catch Github webhooks sending me master thesises and  
forward them to [emailRelay](https://github.com/eldavoo/emailRelay) .  

I didn't like other full-featured solutions, I needed something quick.  

## Poglis

Macca did the same thing [here](https://github.com/emilianomaccaferri/poglis).  
If I knew that, I wouldn't have written this code.  