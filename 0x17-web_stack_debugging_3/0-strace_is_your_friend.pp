# Fixing bug while calling curl to a php file
exec { 'fix-wp-settings.php':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/bin/',
}
