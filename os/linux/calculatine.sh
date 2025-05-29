#!/usr/bin/sh

PY_INTERPETER="python3"

echo "***** CALCULATINE LINUX INSTALLER *****"

# Interpreters menu
echo "\nPython interpreters availables\n"
echo "1 - python (default)"
echo "2 - ipython"
echo -n "\nSelect your python interpreter : "
read py_selector

# Check if ipython
if [ $py_selector = "2" ]
then
    echo "\nYou selected ipython as interpreter.\n"
    PY_INTERPETER="ipython3"
else
    echo "\nYou selected python as interpreter.\n"
fi

# Check if .local/share/applications directory exists
if [ -e $HOME/.local/share/applications/ ]
then
    echo "1. \"$HOME/.local/share/applications\" already exists."
else
    echo "1. Create \"$HOME/.local/share/applications\"."
    mkdir -p $HOME/.local/share/applications
fi

echo "2. Create \"$HOME/.local/share/applications/calculatine.desktop\"."

# Create desktop launcher
cat > $HOME/.local/share/applications/calculatine.desktop <<EOF
[Desktop Entry]
Version=1.0.2
Name=Calculatine
Description=On dit CHOCOLATINE!
Icon=$PWD/chocolatine.ico
Exec=$PY_INTERPETER -i $PWD/calculatine.py
Terminal=true
StartupNotify=true
Type=Application
Categories=System;
EOF

# Final message
echo "\nCalculatine has been installed."
