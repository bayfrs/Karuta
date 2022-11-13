
<p align="center">
<img src="https://raw.githubusercontent.com/bayfrs/Karuta/main/20221111_001827.png" alt="Karuta" width="100"/>


</p>
<p align="center">
<a href="#"><img title="KARUTA MULTI DEVICE" src="https://img.shields.io/badge/KARUTA MULTI DEVICE-green?colorA=%23ff0000&colorB=%23017e40&style=for-the-badge"></a>
</p>

<p align="center">
  <a href="https://github.com/bayfrs/Karuta#requirements">Requirements</a> •
  <a href="https://github.com/bayfrs/Karuta#instalasi">Installation</a> •
  <a href="https://github.com/bayfrs/Karuta#thanks-to">Thanks to</a> •
  <a href="https://github.com/bayfrs/Karuta#Official-Group"> Official Group Bot</a> •
  <a href="https://github.com/bayfrs/Karuta#donate">Donate</a>
</p>
</div>


---

## Information
> Karuta adalah bot multi device tanpa enc . Karuta is a bot whatsapp using a Baileys library.
> Jika kamu menemukan semacam bug, harap untuk dimaklumi sementara

## Bugs and Tester
* Jika kamu menemukan bug jangan lupa buka Issues


# Requirements
* [Node.js](https://nodejs.org/en/)
* [Git](https://git-scm.com/downloads)
* [FFmpeg](https://github.com/BtbN/FFmpeg-Builds/releases/download/autobuild-2020-12-08-13-03/ffmpeg-n4.3.1-26-gca55240b8c-win64-gpl-4.3.zip) (for sticker command)

# Instalasi
## Heroku Buildpack
```bash
heroku/nodejs
https://github.com/jonathanong/heroku-buildpack-ffmpeg-latest
https://github.com/clhuang/heroku-buildpack-webp-binaries.git
```
## For Termux
```ts
pkg update && upgrade 
pkg install git
pkg install nodejs 
pkg install ffmpeg 
pkg install imagemagick 
pkg install python
termux-setup-storage 
git clone https://github.com/bayfrs/Karuta.git
cd Karuta
python Karuta.py
unzip karuta.zip
cd karuta 
npm start
```

## Edit file
<b>buka folder </b>(`/karuta/naimi.js/`)
<br/><b>cari dan ganti dengan nomer owner</b>
```ts
6283149431725@s.whatsapp.net
```
<b>buka folder</b>
(`/src/settings.js`)
```ts
{
     "ownerNumber": ["6283149431725@s.whatsapp.net"],
     "owner": "6283149431725",
     "owner1": ["6283149431725"],
     "packname": "KarutaMD",
     "author": "Karuta",
     "sessionName": "karuta",
     "deskripsi": "Jangan chat kalo gk penting",
     "ownerName": "Karuta",
     "prefix": "#",
     "botName": "Karuta"
}

```

## Donate
- [Trakter](https://wa.me/6281575886399?text=Bang+mau+donasi)
