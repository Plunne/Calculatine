#!/usr/bin/sh

PY_INTERPETER="python3"

echo -e "\n***** CALCULATINE LINUX INSTALLER *****"

# Interpreters menu
echo -e "\nPython interpreters availables\n"
echo -e "1 - python (default)"
echo -e "2 - ipython"
echo -en "\nSelect your python interpreter : "
read py_selector

# Check if ipython
if [ $py_selector = "2" ]
then
    echo -e "\nYou selected ipython as interpreter.\n"
    PY_INTERPETER="ipython3"
else
    echo -e "\nYou selected python as interpreter.\n"
fi

# Define execute command
PY_CMD="$PY_INTERPETER -i $PWD/../../calculatine.py"


# Check if .local/share/applications directory exists
if [ -e $HOME/.local/share/applications/ ]
then
    echo -e "1. \"$HOME/.local/share/applications\" already exists."
else
    echo -e "1. Create \"$HOME/.local/share/applications\"."
    mkdir -p $HOME/.local/share/applications
fi

echo -e "2. Create \"$HOME/.local/share/applications/calculatine.desktop\"."

# Create desktop launcher
cat > $HOME/.local/share/applications/calculatine.desktop <<EOF
[Desktop Entry]
Version=1.0.2
Name=Calculatine
Description=On dit CHOCOLATINE!
Icon=$PWD/chocolatine.ico
Exec=$PY_CMD
Terminal=true
StartupNotify=true
Type=Application
Categories=System;
EOF

# Create bin file
BIN_PATH="/usr/bin/calculatine" 

echo -e "3. Create \"$BIN_PATH\" executable."

cat > $BIN_PATH <<EOF
#!/bin/sh
$PY_CMD
EOF

chmod +x $BIN_PATH

# Final message
echo -e "\nCalculatine has been installed."
