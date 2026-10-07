#!/bin/bash
declare -A clerks=(
["Miami-Dade"]="miamidadeclerk.gov" ["Broward"]="browardclerk.org" ["Palm Beach"]="mypalmbeachclerk.com" ["Hillsborough"]="hillsclerk.com" ["Orange"]="orclerk.com"
["Duval"]="coj.net/clerk" ["Pinellas"]="mypinellasclerk.org" ["Lee"]="leeclerk.org" ["Polk"]="polkcountyclerk.net" ["Brevard"]="brevardclerk.us"
)
for county in "${!clerks[@]}"; do
    echo "$county: https://${clerks[$county]}"
done
