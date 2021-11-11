$option = $args[0]
Write-Output "Sample Installer Script"
Write-Output $option
# Install
if ($option -eq "install") {
    Write-Output "This is the installation part of the script."
}
elseif ($option -eq "update") {
    Write-Output "This is the updation part of the script."
}
elseif ($option -eq "remove") {
    Write-Output "This is the removal/uninstallation part of the script."
}
