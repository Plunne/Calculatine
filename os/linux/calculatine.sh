#!/bin/sh

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
PY_CMD="$PY_INTERPETER -i $PWD/calculatine.py"

# Application path
APP_PATH=$HOME/.local/share/applications
APP_EXEC=$APP_PATH/calculatine.desktop

# Check if .local/share/applications directory exists
if [ -e $APP_PATH ]
then
    echo -e "1. \"$APP_PATH\" already exists."
else
    echo -e "1. Create \"$APP_PATH\"."
    mkdir -p $APP_PATH
fi

# Create desktop launcher
echo -e "2. Create \"$APP_EXEC\"."

cat > $APP_EXEC <<EOF
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
BIN_PATH=$HOME/.local/bin
BIN_EXEC=$BIN_PATH/calculatine

# Check if .local/bin directory exists
if [ -e $BIN_PATH ]
then
    echo -e "3. \"$BIN_PATH\" already exists."
else
    echo -e "3. Create \"$BIN_PATH\"."
    mkdir -p $BIN_PATH
fi

echo -e "4. Create \"$BIN_EXEC\" executable."

cat > $BIN_EXEC <<EOF
#!/bin/sh
$PY_CMD
EOF

chmod +x $BIN_EXEC

# Final message
echo -e "\nCalculatine has been installed."
