wsl --list --quiet
ollama run gpt-oss:120b-cloudwsl --set-default-version 2
wsl --set-version <distro> 2

ollama serve gpt-oss:120b-cloud
