#!/bin/bash

# Function to download and rename the file
download_and_rename() {
    local url=$1
    local new_name=$2
    echo "Downloading from URL: $url"

    if command -v wget &> /dev/null; then
        wget --show-progress --progress=bar:force --output-document=temp_file "$url"
    elif command -v curl &> /dev/null; then
        curl --progress-bar --location --output temp_file "$url"
    else
        echo "Neither wget nor curl is installed."
        exit 1
    fi

    # Check the downloaded file size
    local file_size=$(stat --format="%s" temp_file 2>/dev/null || stat -f%z temp_file)
    echo "Downloaded file size: $file_size bytes"

    if [ $file_size -gt 1000 ]; then  # Assuming anything below 1 KB is suspicious
        mv temp_file "$new_name"
        echo "File downloaded and renamed to $new_name"
    else
        echo "Downloaded file is too small, likely an error page. Check the file content."
        cat temp_file
        rm -f temp_file
        exit 1
    fi
}

# Direct URLs for each file
declare -A URLS=(
    [1]="https://figshare.com/ndownloader/files/46997677?private_link=bbb0c2463e8c8a24814a"
    [2]="https://figshare.com/ndownloader/files/46976903?private_link=bbb0c2463e8c8a24814a"
    [3]="https://figshare.com/ndownloader/files/46976904?private_link=bbb0c2463e8c8a24814a"
    [4]="https://figshare.com/ndownloader/files/46976905?private_link=bbb0c2463e8c8a24814a"
    [5]="https://figshare.com/ndownloader/files/46976906?private_link=bbb0c2463e8c8a24814a"
    [6]="https://figshare.com/ndownloader/files/46976907?private_link=bbb0c2463e8c8a24814a"
    [7]="https://figshare.com/ndownloader/files/46976908?private_link=bbb0c2463e8c8a24814a"
    [8]="https://figshare.com/ndownloader/files/46976909?private_link=bbb0c2463e8c8a24814a"
    [9]="https://figshare.com/ndownloader/files/46976910?private_link=bbb0c2463e8c8a24814a"
    [10]="https://figshare.com/ndownloader/files/46976911?private_link=bbb0c2463e8c8a24814a"
)

# Filenames corresponding to the options
declare -A FILENAMES=(
    [1]="2DbubbleGroup1_npz.tar.gz"
    [2]="2DdropGroup1_npz.tar.gz"
    [3]="2DdropGroup2_npz.tar.gz"
    [4]="2DbubbleGroup2_npz.tar.gz"
    [5]="2DdropGroup3_npz.tar.gz"
    [6]="2DbubbleGroup3_npz.tar.gz"
    [7]="2DdropGroup4_npz.tar.gz"
    [8]="2DdropGroup5_npz.tar.gz"
    [9]="2DbubbleGroup4_npz.tar.gz"
    [10]="2DbubbleGroup5_npz.tar.gz"
)

# Prompt user to choose an option
echo "Please choose an option (1-10):"
echo "1. Download 2DbubbleGroup1_npz.tar.gz"
echo "2. Download 2DdropGroup1_npz.tar.gz"
echo "3. Download 2DdropGroup2_npz.tar.gz"
echo "4. Download 2DbubbleGroup2_npz.tar.gz"
echo "5. Download 2DdropGroup3_npz.tar.gz"
echo "6. Download 2DbubbleGroup3_npz.tar.gz"
echo "7. Download 2DdropGroup4_npz.tar.gz"
echo "8. Download 2DdropGroup5_npz.tar.gz"
echo "9. Download 2DbubbleGroup4_npz.tar.gz"
echo "10. Download 2DbubbleGroup5_npz.tar.gz"
read -p "Enter your choice: " choice

# Validate user input
if [[ ! $choice =~ ^[1-9]$|^10$ ]]; then
    echo "Invalid option. Please choose a number between 1 and 10."
    exit 1
fi

# Download and rename based on user choice
URL=${URLS[$choice]}
NEW_NAME=${FILENAMES[$choice]}

download_and_rename "$URL" "$NEW_NAME"
