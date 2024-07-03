import argparse
import os
import time
import sys
import base64


def AH_CTF():
    PASSWORD_FILE = base64.b64decode("cGFzc3dvcmQudHh0").decode() # "password.txt"  # File containing the password
    PASSWORD = base64.b64decode("aWd1YW5h").decode()  # "iguana"
    KEY = base64.b64decode(
        "TElaQVJEe0wxekByZE1Ac3Qzcn0="
    ).decode()  # LIZARD{L1z@rdM@st3r}

    class CtfFiles:
        def __init__(self, password):
            self.files = {
                "hint.txt": f'There are some hidden files in the program, such as "{PASSWORD_FILE}"',
            }
            self.hidden_files = {PASSWORD_FILE: "Password is: " + PASSWORD}
            if password == PASSWORD:  # the password show more files
                self.files = {
                    **self.files,
                    **{
                        "prophecy_of_vitruvius.png": "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",
                        "cool_prophecy.png": "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",
                        "smiley.png": "iVBORw0KGgoAAAANSUhEUgAAAZAAAAGQCAIAAAAP3aGbAAANi0lEQVR4nO3d3XbixhaFUTmj3/+VfS7o4zgChBD62WvXnJfJSEdU7foksNv++v7+ngAS/HP1BQCsJVhADMECYggWEEOwgBiCBcQQLCCGYAExBAuIIVhADMECYggWEEOwgBiCBcQQLCCGYAExBAuIIVhADMECYggWEEOwgBiCBcQQLCCGYAExBAuIIVhADMECYggWEEOwgBiCBcQQLCCGYAExBAuIIVhADMECYggWEEOwgBiCBcQQLCCGYAExBAuIIVhADMECYggWEEOwgBiCBcQQLCCGYAExBAuI8efqCyDP19fXXn/U9/f3Xn8UI/gyMTy0Y5W2MZncEyymqUCe1jCrCNagIgq1zOgOSLAG0iBSzxjjQQhWc0dEaseZKX55VCNYPe0SggtnI/36OYhgtfLJOS8+CY1fGusJVgfbDnP01g/4kpkEK9qGQ9tyu63DOAQrz7vnc6gttji9CVaS9afRtk6WqyPByrDy7NnNh6xeG4JVmpO2L+uZTrCKcrSOY21zCVY5a46TXduFpY4jWIU4P5ew7EEEq4SXZ8Y2ncAu1CdYF3NIqrEjlQnWlZbPhq25kK2pSbCu4TxEsE3VCNbZnIE4tqwOwTqPuY9m+yoQrJMsjLstCGIfryVYh3NnbsaGXkiwjuWG3JWdvYRgHcVAj8Aun+yfqy+gJ3M8iIXdbPxL1S7kCWt/zybVUjdm088hWHvyYDUyu38CwdqNeyyTMTiYz7D2YUy5ebbjPtLahSesT0kVDxmMI3jC+oih5BmPWkcQrO3UimWatTtvCTd6OHMWk4dMy14E620erNjA2OzCW8L3GDu28fZwF56w3uDBns+Zok94wlrLnLGLhzPjOWslwVpFrdiRZm0mWK+pFbvTrG0E6wW14iCatYFgLVErDqVZ7xKsp9SKE2jWWwTrMbXiNJq1nmA9oFacTLNWEqw5teISmrWGYP2HWnEhzXpJsP6lVlxOs5YJ1l9qRRGatUCwpkmtKEaznhEstaIizXpIsB5QKyowh/dGD9b9LcuUUMf9NA7+kDV0sNSK+jTrt3GDpVak0KwfgwZLrciiWTeDBgtINGKwPF6RyEPWNGCw1IpcmjVWsNSKdIM3a6xgAdEGCpbHK3oY+SFrlGCpFZ0M26whgqVW9DNms4YIFtBD/2B5vKKrAR+ymgdLrehttGY1DxbQyVfjJ45Oj1cLt83cF3WJlivZadSXtQ1Wgy3c8Gwf9xrPMcJKNhj4Nf5cfQE8sPljiNt/2HJSt7GSzfR8wsq92+z4iWnKSz7IgCuZO/brDRGsiNd40Bd3Il77vkZeycTJf0vDrxImfln3uGtOXI1PWMnfEq95WcNgzdS/yRw9Vf2m9hkrWX/aP9QtWPVHauacC45blg2s5ENxF7ysVbDiPnQ8c5iaDe6MlfzR+3vfWwVrRq0u/z+ew0rOFJ/8T/QJVvEZmrnqarNWaQ0ruUbW1S7oE6yZyjeZa6enzexOV7+WyitZef4/0SRYlUcHKuhxRpoEa6by7aXC3FS4hs9VeBUVruGZyqdgsw7Bqjw0UEeDk9IhWDOVbyx1JqbOlWxT5/rrXMm9ymdhm/hgVR4XqCb9vMQHa6byLaXarFS7nvWqXXm16/mt8onYIDtYlQcFaoo+NdnBmml2M4FddDoXrYIF9BYcrKyfVVbzObzmVS2rec01r+rH7HQUv9oFwcECRpMarNxbBFQQeoJSgzVT/P0gXK7HGYkMVujNAUpJPEeRwZrpceuAozU4KR2CBQwiL1iJz7FQU9xpygvWTIOnXDhN+nmJD1aKmoNS86qW1bzmmlfVT1iwsr67HQqK/q73sGABIxMsIEZSsNLfD1a74GrXs161K692PS/lvitMChYwOME6VZ1bcZ0r2abO9de5khHEBCv9/SCUEvquMCZYbVRIbYVr+FyFV1HhGoYiWECMjGClPK+udO1tudNDgZXcUcQpywjWTINBueolNFi6GSu5WeJLiAxWD+ePS+KArmElxyFYVzpz7nufMSs5iIBgRby13uyc6R/hjFnJz9U/awHBmuk3MUe/on4r9oyVfFfcK8oLVkvHzU3cRH7ISvb25+oL4K/bedjxmXzYA2YlG/sqvhn3Y1f8gnfx4WEbYYlWspIvZR2xsGAVv9p9bThsQ63PelZyWdAp85awrt9zs3DkKo9XEVayDcHK4CztxUpG81VCIEbpYNX/Njbop/K5Kx2sGQ/zcISgk5UULGBwggXEECwghmABMeoGq/KXKqC3sqevbrBmgr6QAXFSzldMsAAEC4ghWEAMwQJiCBYQQ7CAGIIFxCgarKCf2Qo9zE5Zze8dLRosgHuCBcQQLCCGYAExBAuIIVhADMECYggWEEOwgBiCBcQQLCCGYAExBAuIIVhADMECYggWEEOwgBiCBcQQLCCGYAExBAuIIVhADMECYggWEKNosCJ+pyN0EvHbi4sGC+CeYAExBAuIIVhADMECYggWEEOwgBgxwfKtWHCclPNVN1g1v28NRlD29NUNFsCMYAExBAuIIVhAjKRgpXwhA7IEnazSwSr7pQporPK5Kx0sgN8EC4ghWECMsGAFfToIEbLOVPVgVf78D/opfuKqBwvgh2ABMfKClfWWGyqLO00BwSr+phraqH/WAoIFcCNYQIzIYMW98YaCEs9RRrDqv7WGdBGnLCNYAJNgAUFigjV7Xk18+w11zE5QxPvBKShYAIIFxEgKlneFsIvQ94NTVrCAwQkWEOMr6GnwJvdp9iAWZJn1mYleEE9YQIz4YPnoHdZLPy95wcp6goXK4k5TXrCAYXUIVvpTLpyjwUmJDFbccywUlHiOIoN1r8GtYy+W4jer8aPHUqQGK/HmcBBLsZ61+hG6FKnBAgYUHCx/FxpWiv7u9t+CgwWMplWwPGTdWIcb63DTaR2yg5X7ZLsv67CGVbqJXofsYN3rdDOBzzU7EfHBir5dHKfZmG5gBR5KPy/xwbo35qSmD+LRxlyffmehQ7DGnEV4V4OT0iFY9/rdWDYYeRFGfu0/Wi5Ck2A1uHV8ziI8Y2WmLovQJFj3Wt5e3jXmIoz5qme6LkKfYPW4gXzIItyzJlOjRegTrHtdbzJvGW0RRnu9DzVehFbBur+NNN65Z9rcS3cx4Grcz3ynRWgVrKnX3uxlnGqP80rXa3YiugXr3oBD3GxGNxtwHdpPe8NgDTimL7Wf42mM1/iufmehYbDuDTjKo32c1/uDm5V6b/FNz2CNdlwfGmcR1GoaZhF6BgtoqW2wxnm+WDDCIgzyZLFsnEVoG6xpjOP6Uu9FGOegLhhqEToHi5uuzRrqoHLTPFhdz+rn0tch/fr3Mlq1mwdr0qxpmp4Mce46PLzy3gf1odFqNY0QLG7aNEutRvY1yE4PeC966FmhIlYj+uJ3N+ZIj/KE5Y3hzbOZrr8aavXbmLWaxgnWpFn/l9gstfpt2FpN0/Tn6gvgArf5vp/72z8pNf1SxW+jfIb1Y+S7072Fp6rLl6XytV1o8AEeLljT8Fs+s/xO8JKVKXhJRRjdEYM12fg7RRpR5DJqMrSTz7C4+f7+XojFz7866ISs+bx/wMPJvUGfsCb3qydWfq1wl7U68/+VzrjejBusyRA89+63OKxct4P+2PYM6o+hgzUZhUUXfmeWXfhhRH8bPViTgXjl5GxZ/N8M54wP3R/4+tLxf/0sxaHlsuD3Kv/dg6s4mdPkBwC8aceDZJGfMZMPCdZf5mOzt/plSdcwjc8I1r9MCRWYwwUD/bSGl9r8iDtyqdUywfoPzeJCavWSYM1pFpdQqzUE6wHN4mRqtZJgPaZZnEat1hOspzSLE6jVWwRriWZxKLV6l2C9oFkcRK02EKzXNIvdqdU2grWKZrEjtdpMsNbSLHahVp/wdwnf49fksZnh+ZwnrPck/tpkKlCrXXjC2siDPeuZlr0I1nbumbxkSPblLeF23h6yTK12J1gf0SyeUasjeEu4D9PJD8NwHE9Y+/CoxY1aHcoT1p4W8mSd27P7JxCs/bnHDsimn0OwDuFmOw57fSafYR1iYVJ9qtWJWp3ME9axDHRXdvYSgnW45Ucq6x/Hhl5IsE7ihtyDfbyWYJ3HnTma7atAsM5m7uPYsjoE6xrOQATbVI1gXcl5KMvW1CRYF3v5bVk26GR2pDLBKsEhqcAu1CdYhaz5Jnj7tTvLHkSwynF+TmOp4whWUSv/yqHt28Da5hKs0hytfVnPdIKVwUn7hNVrQ7CSrP/RNLZ1slwdCVaed3+i1lBbbHF6E6xgG34WYMvttg7jEKwOtv0U0+itH/AlMwlWM5/8/OXik9D4pbGeYPW0y0+Ov3A20q+fgwhWc0f8zosdZ6b45VGNYA2k8S/sMcaDEKxBNYiX0R2QYDFNIf0yqwgWj12eMJPJPcHibTu2zPjxFsECYvxz9QUArCVYQAzBAmIIFhBDsIAYggXEECwghmABMQQLiCFYQAzBAmIIFhBDsIAYggXEECwghmABMQQLiCFYQAzBAmIIFhBDsIAYggXEECwghmABMQQLiCFYQAzBAmIIFhBDsIAYggXEECwghmABMQQLiCFYQAzBAmIIFhBDsIAYggXEECwghmABMQQLiCFYQAzBAmIIFhBDsIAYggXEECwghmABMf4HJLabM1R6nZMAAAAASUVORK5CYII=",
                        "cool_smiley.png": "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",
                        "flag.txt": "R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7",
                    },
                }

        def list_files(self):
            return self.files.keys()

        def save_file_to_downloads_folder(self, filename, data, is_base64=False):

            def get_unique_filename(directory, filename):
                base, extension = os.path.splitext(filename)
                counter = 1
                unique_filename = filename

                while os.path.exists(os.path.join(directory, unique_filename)):
                    unique_filename = f"{base} ({counter}){extension}"
                    counter += 1

                return unique_filename

            downloads_dir = os.path.join(os.path.expanduser("~"), "Downloads")
            file_path = os.path.join(downloads_dir, filename)

            if os.path.exists(file_path):
                filename = get_unique_filename(downloads_dir, filename)
                file_path = os.path.join(downloads_dir, filename)

            # add effect of loading
            print("Downloading...")
            time.sleep(2)

            # save file
            if is_base64:
                data = base64.b64decode(data)
            with open(file_path, "wb" if is_base64 else "w") as f:
                f.write(data)

            # add effect of loading
            print(f'Download complete! File saved at "{file_path}"')

        def download_file(self, filename):
            if filename not in self.files and filename not in self.hidden_files:
                print(f'ERROR: File "{filename}" not found in program')
                return

            data = self.files.get(filename, self.hidden_files.get(filename))
            is_base64 = filename.endswith(".png")

            self.save_file_to_downloads_folder(filename, data, is_base64)

    def main():
        parser = argparse.ArgumentParser(
            prog="python ah-ctf.pyc",
            description="Welcome to my CTF!\nCapture the flag to save the lizards' kingdom!",
            epilog="Remember: cheat by using notepad++ is valid (but it's not the only way to win!)",
            formatter_class=argparse.RawTextHelpFormatter,
        )
        parser.add_argument(
            "-p",
            "--password",
            help="Password for program. Note: There are some passwords in the program",
        )
        parser.add_argument("-d", "--download", help="Download file")
        parser.add_argument("-k", "--key", help="Insert the key to win the CTF")
        parser.add_argument(
            "-l", "--list", action="store_true", help="List files in program"
        )

        if len(sys.argv) < 2:
            parser.print_help()
            sys.exit(1)

        args = parser.parse_args()

        if args.key == KEY:
            print(
                r"""   You saved the Lizards !
     \ \ \ \ \ \ \ \ \| |\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \| |\ \ \ \ \ \ \ \ \ 
    / / / / / / / / / | | / / / / / / __  / / / / / / / / | | / / / / / / / / /
     \ \ \ \ \ \ \ \ \| |\ \ \ \ \   /..\  ` ` \ \ \ \ \ \| |\ \ \ \ \ \ \ \ \ 
    ------------------' `---------- (    ) \|/ -----------' `------------------
     ,------------------------- _\___>  <__//` ------------------------------. 
     |/ / / / / / / / / / / / / >,---.   ,-'  / / / / / / / / / / / / / / / /| 
     | \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ |  . \  \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ | 
     |/ / / / / / / / / / / / / / /  `. `. \   ., / / / / / / / / / / / / / /| 
     | \ \ \ \ \ \ \ \ \ \ \ \ \ \ \  |  `. | \||_ \ \ \ \ \ \ \ \ \ \ \ \ \ | 
     |/ / / / / / / / / / / / / / / / `.  : |__||   / / / / / / / / / / / / /| 
     | \ \ \ \ \ \ \ \ \ \ \ \ \ \ \  __> `.,---'  \ \ \ \ \ \ \ \ \ \ \ \ \ | 
     |/ / / / / / / / / / / / / / /  |.--'\`.\  / / / / / / / / / / / / / / /| 
     `------------------------------ _\\   \`.| -----------------------------' 
    ------------------. ,------------ /|\ - |:| ----------. ,------------------
     \ \ \ \ \ \ \ \ \| |\ \ \ \ \ \ ' `    |:|  \ \ \ \ \| |\ \ \ \ \ \ \ \ \ 
    / / / / / / / / / | | / / / / / / / / / |:| / / / / / | | / / / / / / / / /
     \ \ \ \ \ \ \ \ \| |\ \ \ \ \ \ \ \ \  |:/  \ \ \ \ \| |\ \ \ \ \ \ \ \ \ 
    / / / / / / / / / | | / /  --.________,-_/  / / / / / | | / / / / / / / / /
     \ \ \ \ \ \ \ \ \| |\ \ \ \ \ ```-----' \ \ \ \ \ \ \| |\ \ \ \ \ \ \ \ \ 
    / / / / / / / / / | | / / / / / / / / / / / / / / / / | | / / / / / / / hjm"""
            )
            return

        ctf_files = CtfFiles(args.password)

        if args.list:
            print("Files in program:")
            for f in ctf_files.list_files():
                print(" *", f)
        elif args.download:
            ctf_files.download_file(args.download)
        else:
            parser.print_help()

    main()


if __name__ == "__main__":
    AH_CTF()