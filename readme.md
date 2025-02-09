## Set 0.0.0.0

From: https://www.restack.io/p/ollama-serve-answer-windows-0-0-0-0-cat-ai

Also mentioned in official doc: https://github.com/ollama/ollama/blob/main/docs/faq.md

Setting Environment Variables on Linux
For Linux users running Ollama as a systemd service, follow these steps:

Open a terminal and edit the systemd service file:

```sh
systemctl edit ollama.service
```

In the editor, add the following line under the `[Service]` section:

```
[Service]
Environment="OLLAMA_HOST=0.0.0.0"
```

Save and exit the editor.
Reload the systemd configuration and restart Ollama:

```sh
systemctl daemon-reload
systemctl restart ollama
```