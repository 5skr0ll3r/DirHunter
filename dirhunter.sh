#!/bin/bash
#MIT License at the bottom

{
extensions=('' ".html" ".css" ".js" ".txt" ".php" ".py" ".xml")
ping_check=true
logo=true
threads=20

while getopts "h:f:p:sl" opt; do
  case $opt in
	h) host="$OPTARG"
	;;
	f) file="$OPTARG"
	;;
	p) threads="$OPTARG"
	;;
	s) ping_check=false
	;;
	l) logo=false
	;;
	\?) 
		echo "Invalid option -$OPTARG" >&2
		exit 1
	;;
	:)
		echo "Option -$OPTARG requires an argument" 1>&2
		exit 1
	;;
  esac
done

if [ $logo == true ]
then 
	echo -e "\033[35m=====================================================================================\033[0m"
	echo -e "\033[35m
      	 ##    # ###   #   # #       # ##      # ####### ###### ###
      	 # #   # #  #  #   # #       # # #     #    #    #      #  #
      	 #  #  # #   # #   # #       # #  #    #    #    #      #   #
      	 #   # # #  #  #####  #     #  #   #   #    #    ###### #  #
      	 #  #  # # #   #   #   #   #   #    #  #    #    #      # #
      	 # #   # #  #  #   #    # #    #     # #    #    #      #  #
      	 ##    # #   # #   #     #     #      #     #    ###### #   #\033[0m\n"
      echo -e "\033[35m=====================================================================================\033[0m"
fi

#check if enough arguments are specified
if [ -z "$host" ] || [ -z "$file" ]
then
  echo -e "\033[32mUsage: $0 -h host -f file [-p threads] [-s] [-l] \n\t-s: Disables ping\n\t-p: Set's thread count (Default threads: $threads)\n\t-l Desables the logo (Default is on)\033[0m"
  exit 1
fi

#Remove return-cariege and new-line from host
host=`echo $host | tr -d "\r\n "`


# Send a GET request to the target using HTTP
check=$(curl -s -I "http://$host/")


# Check if the response contains "HTTP/1." (indicating HTTP protocol)
if [[ $check == *"HTTP/1."* ]]; then
    prefix="http"
else
    prefix="https"
fi


#check if ping is set cause if host has icmp disabled the script will exit even if the host is alive
if [ $ping_check == true ]
then
	host_is_up=` ping -c 3 "$host" 2> /dev/null | grep -m 2 "64 bytes from" `
	if [ -z "$host_is_up" ]
	then
	      echo -e "\033[32mHost \033[31m$host\033[32m is \033[31mnot\033[32m responding\nCheck the target typed and try again\033[0m"
	      exit 1
	else
	      echo -e "\033[32mHost \033[35m$host\033[32m responded\033[0m"
	fi
fi


#check if file specified exists
if [ ! -f "$file" ]
then
	echo -e "\033[31mThe File you specified does not exist\033[0m"
	exit 1
else
	echo -e "\033[32mFile Located\033[0m"
fi


# Define a function to stop all running threads
stop_threads() {
    echo -e "\n\033[32mKilling all running threads...\033[0m"
    pkill -P $$
    echo -e "\033[35m=============================\033[0m"
    exit 2
}


# Trap the SIGINT signal (CTRL+C) and call the stop_threads function
trap 'stop_threads' SIGINT


#Claculates the number of lines each thread will read
lines=`wc -l $file | awk -F ' ' '{ print "",$1 }'`
each_thread=$((lines / threads))

echo -e "\033[35m=============================\033[0m"

start=1
for (( x=1; x<=$threads; x++ ))
do
	{
	for (( i=$start; i<=$((start + each_thread)); i++))
	do
		current_line=`head -n $i $file | tail -1`
		if [[ $current_line == "#"* ]]
		then
			continue
		else
			sleep .1
			for ex in "${extensions[@]}"
			do
				extension=`echo "$ex" | tr -d "\r\n "`
				#Remove return-carieges and new-lines from target 
				target=`echo "$prefix://$host/$current_line$extension" | tr -d "\r\n "`
				page_nexists=`curl -I --silent "$target" 2>&1 | grep 404` 
				if [ -z "$page_nexists" ]
				then
					echo -e "\033[31m-> \033[35m$prefix://$host\033[0m\033[32m/$current_line$extension\033[0m" | tr -d "\r"
				else
					continue;
				fi
			done
		fi
	done 
	} & 


	start=$((start + each_thread))
done



# Wait for all child processes to finish
wait  	

echo -e "\033[35m=============================\033[0m"

echo -e "\n\033[32mAll child processes completed successfully.\033[0m\n"
} 2>/dev/null


#MIT License

#Copyright (c) 2020 5skr0ll3r

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.
