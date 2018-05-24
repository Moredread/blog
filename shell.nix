with import <nixpkgs> {};

stdenv.mkDerivation {
  name = "blog";
  buildInputs = [
    gnumake
    python27Packages.markdown
    python27Packages.pelican
    python27Packages.piexif
    python27Packages.typogrify
  ];
}