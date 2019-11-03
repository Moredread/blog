with import <nixpkgs> {};

stdenv.mkDerivation {
  name = "blog";
  buildInputs = [
    gnumake
    python3Packages.markdown
    python3Packages.pelican
    python3Packages.piexif
    python3Packages.typogrify
  ];

  src = ./.;

  preBuildPhase = "rm -rf output";

  buildFlags = "publish";

  installPhase = ''
    mkdir -p $out
    cp -r output/* $out
  '';
}
