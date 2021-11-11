$option = $args[0]
Write-Output "Sample Installer Script"
Write-Output $option
# Install
if ($option -eq "-i") {
    Write-Output "This is the installation part of the script."
}
elseif ($option -eq "-u") {
    Write-Output "This is the updation part of the script."
}
elseif ($option -eq "-r") {
    Write-Output "This is the removal/uninstallation part of the script."
}