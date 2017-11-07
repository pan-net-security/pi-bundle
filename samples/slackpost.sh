#!/usr/bin/env bash

# to be used with e.g gbexec (https://github.com/operable/gbexec)
# docker run --rm -v $PWD:/samples -w /samples gbexec:dev -s token_delete.greenbar token_delete.json | ./slackpost.sh <SLACK-TOKEN-URL> <some_channel> [some_username]
#
# 
# ------------

webhook_url=$1
if [[ $webhook_url == "" ]]
then
        echo "No webhook_url specified"
        exit 1
fi

# ------------
shift
channel=$1
if [[ $channel == "" ]]
then
        echo "No channel specified"
        exit 1
fi

# ------------
shift
username=$1
if [[ $username == "" ]]
then
        username="slackpost"
fi

# ------------
shift

escapedText=$(echo $text | sed 's/"/\"/g' | sed "s/'/\'/g" )

attachment_stdin=`cat -`
escaped_stdin=$(echo $attachment_stdin | sed 's/"/\"/g' | sed "s/'/\'/g" )

echo "$escaped_stdin"
json="{\"channel\": \"$channel\", \"username\":\"$username\", \"icon_emoji\":\"ghost\", \"attachments\": $escaped_stdin}"


curl -s -d "payload=$json" "$webhook_url" 
