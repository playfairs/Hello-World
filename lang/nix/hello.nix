with import <nixpkgs> {};

stdenv.mkDerivation {
  name = "hello";
  buildCommand = ''
    echo "Hello, World!"
  '';
}
