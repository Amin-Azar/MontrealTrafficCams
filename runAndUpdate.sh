
while :
do
    echo "Running @ $(date)"
    # grab new images and analyze
    python3 analyze-image.py
    python3 detection.py
    # push to the repo/ github page
    git pull
    git add data_out reports images images_out
    git commit -m "updated for $(date)"
    git push origin gh-pages
    # wait for next round
    sleep 1800 # every half hour / AZURE turned off
done
