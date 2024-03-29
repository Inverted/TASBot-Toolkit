**To use with [tasbot_eyes](https://github.com/R3tr0BoiDX/tasbot_eyes)**

---

# aNinja
***An**imation **Inj**ecto***a***r*

Inject any wished animation into the current animation stack. Uses a UDP socket to communicate with TASBots eyes. Path can be relative or absolute.

### ⚠️ Attention
* The path to the animation is a path to an animation, that is already stored locally on TASbot. This tool does **NOT** transfer any animation files to TASBot. It just plays an already locally stored animation on TASBot. Relative paths are relative to current working directory **the TASBot eye software is running in**.

## Usage
Adjust the IP in `aninja.py:5` to TASBots one.

`python3 aninja.py [-I] <path on TASBot to animation>`
* `-I`: Plays the animation immediately

---

# BECAUSE
*TAS**B**ot **E**ye **C**olor **A**nalyzing **U**niquified **S**earch **E**ngine*

Converts any given file into a color palette, that can be used with the TASBot eye controller software

### ⚠️ Attention
Program loops over all pixels of the image. Be careful with larges images. Meant to be used with small files, only a few dozen pixels big!

## Usage
`python3 because.py <path to image>`

## Future ideas
Prevent the color black (`0x000000`) to be added to the palette. Alternatively, the luminance of the color could be calculated first and there could be a threshold, for how dark colors can get.
