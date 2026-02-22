# uv run -m usrbot

hour=3600 # 1 hour
timer=$((hour*6))


while true;do
    timeout $timer uv run -m usrbot
    echo "Restarting"
<<<<<<< HEAD
    
=======
    bash stop
>>>>>>> de03dc118fb272d0903777d18d5a9cc17889d2a7
    sleep 1
done
