#!/bin/bash

#------------------------------------------------------------------------------
# This script creates solution templates
#
# Liang Lin
#------------------------------------------------------------------------------
exec 7>&1           # write to output file.
exec > /dev/stderr  # Redirect current stdout to stderr

get_template() {
    case ${!1} in
    j)  eval $1="Solution.java";     return 0;; 
    p)  eval $1="solution.py";       return 0;;
    m)  eval $1="question.md";       return 0;;
    *)  return 1;;
    esac
}

ask() {
    local i=$((54 - ${#1}))
    local p
    printf -v p "%*s" $i
    echo -n "${1}${p// /.}: " 
}

year=$(date +%Y)
now=$(date +%Y-%m-%d)
#author=$(awk -F: 'user == $1 {print $5}' user=$USER /etc/passwd)
author=$(git config --get user.name 2> /dev/null)
copyright="$author"
def_email=$(git config --get user.email 2> /dev/null)
tabwidth=4

while getopts 'hf:e:t:c:o:w:' OPTION ; do
    case $OPTION in
    c)  [ -n "$OPTARG" ] && copyright="$OPTARG"
        copyrt=1;;
    e)  email="$OPTARG";;
    f)  markdown="$OPTARG";;
    t)  template="$OPTARG"
		get_template template
        if [ $? -ne 0 ]; then
           echo "Invalid template type: $template" 
           exit 1
        fi;;
    o)  # Redirect output to file
        [ -d "$OPTARG" ] || (echo "$OPTARG directory doesn't exist!"  && exit 1)
        outdir="$OPTARG"
        ;;
    w)  tabwidth=$OPTARG
        [ $tabwidth -eq 2 -o $tabwidth -eq 4 ] || (echo "Tabwidth must be 2 or 4!" && exit 1);;

    *)  echo "This script creates generic solution files from templates."
        echo
        echo "Usage: $0 [-f File] [-e Email]" 
        echo "          [-c Copyright] [-o OutputDir] [-w TabWidth]" 
        echo "  Type        - j  = java solution"
        echo "                p  = python solution"
        echo "                m = markdown"
        echo "  OutputDir   - when provided, output is redirected to "
        echo "                OutputDir/file'"
        exit 1;;
    esac
done

while [ -z "$template" ]; do
    echo "Create a solution template in [(j)ava), (p)ython,"
    ask  "                               (m)arkdown]"
    read template && get_template template && break
    unset template
done

while [ -z "$file" ]; do
    ask "solution file"
    read file && [ -n "$file" ] && break
done

while [ -z "$email" ]; do
    if [ -n "$def_email" ]; then
        m=" [default: $def_email]"
    fi
    ask "Email address${m}"
    read email && [ -n "$email" ] && break || email="$def_email"
done

if [ -n "$outdir" ]; then
    outfile="$outdir/$file"
    echo "Creating file: $outfile" 
    exec > "$outfile" || exit 1
else
    exec 1>&7   # Restore old file descriptor
fi
    
dir=$PWD

sed -e "s!%AUTHOR%!${author}!g" \
    -e "s!%DATE%!${now}!g" \
    -e "s!%EMAIL%!${email}!g" \
    -e "s!%TITLE%!${outdir}!g" \
    ${dir}/${template}.in

exec 1>&7 7>&-       # Restore stout
s
if [ -n "$outfile" ]; then
    echo "git add $outfile"
    git add $outfile
    echo "git commit $outfile"
    git commit -m "add $outfile" $outfile
    echo "git push"
    git push
else
    exec 1>&7
fi
