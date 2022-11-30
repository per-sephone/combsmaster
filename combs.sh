#!/bin/bash
i=0
until [[ "$(md5sum <(echo -n "${i}d470d406"))" =~ "0badbeef" ]]
do
    i=$((i+-1))
    echo "$(md5sum <(echo -n "${i}d470d406"))"
    echo $i
done

echo "${i}d470d406"
