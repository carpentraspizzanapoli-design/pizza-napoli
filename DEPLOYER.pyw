"""
Déployeur Pizza Napoli Carpentras
Double-clic → colle le token Netlify → déploiement automatique
"""
import tkinter as tk
from tkinter import ttk, messagebox
import threading, urllib.request, json, os, io, zipfile, webbrowser

SITE_ID  = 'astonishing-lokum-0e4892'
SITE_URL = 'https://www.pizzanapolicarpentras.fr'
HERE     = os.path.dirname(os.path.abspath(__file__))

IMG_EXT  = {'.jpg','.jpeg','.png','.webp','.gif'}
COPY_EXT = {'.html','.toml','.txt','.xml','.ico','.svg','.json','.woff','.woff2','.ttf','.eot'}
SKIP_EXT = {'.py','.pyw','.pdf','.pyw'}
SKIP_DIR = {'__pycache__', '.git', '.claude'}

MAX_W, MAX_H, QUALITY = 1920, 1400, 82

try:
    import PIL.Image as Image
    HAS_PIL = True
except ImportError:
    HAS_PIL = False


def build_zip():
    buf = io.BytesIO()
    n = 0
    with zipfile.ZipFile(buf, 'w', zipfile.ZIP_DEFLATED, compresslevel=6) as zf:
        for root, dirs, files in os.walk(HERE):
            dirs[:] = [d for d in dirs if d not in SKIP_DIR and not d.startswith('.')]
            for fname in files:
                if fname.startswith('.'): continue
                ext = os.path.splitext(fname)[1].lower()
                if ext in SKIP_EXT or fname in ('DEPLOYER.pyw',): continue
                fpath = os.path.join(root, fname)
                relpath = os.path.relpath(fpath, HERE).replace(os.sep, '/')
                if ext in IMG_EXT and HAS_PIL:
                    try:
                        with Image.open(fpath) as im:
                            if im.mode not in ('RGB', 'L'):
                                im = im.convert('RGB')
                            w, h = im.size
                            if w > MAX_W or h > MAX_H:
                                im.thumbnail((MAX_W, MAX_H), Image.LANCZOS)
                            ibuf = io.BytesIO()
                            im.save(ibuf, 'JPEG', quality=QUALITY, optimize=True, progressive=True)
                            zf.writestr(relpath, ibuf.getvalue())
                            n += 1
                            continue
                    except Exception:
                        pass
                if ext in COPY_EXT or ext in IMG_EXT:
                    with open(fpath, 'rb') as f:
                        zf.writestr(relpath, f.read())
                    n += 1
    return buf.getvalue(), n


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Déployer — Pizza Napoli Carpentras')
        self.geometry('500x320')
        self.resizable(False, False)
        self.configure(bg='#0a0a0a')
        self._build()

    def _build(self):
        tk.Label(self, text='PIZZA NAPOLI CARPENTRAS', bg='#0a0a0a',
                 fg='#d4af37', font=('Arial', 12, 'bold'), pady=14).pack()
        tk.Label(self, text='Déploiement Netlify automatique', bg='#0a0a0a',
                 fg='#333', font=('Arial', 9)).pack()

        tk.Frame(self, bg='#1a1a1a', height=1).pack(fill='x', pady=10)

        # Step 1 — open Netlify
        f1 = tk.Frame(self, bg='#0a0a0a', padx=24)
        f1.pack(fill='x')
        tk.Label(f1, text='① Génère un token Netlify :', bg='#0a0a0a',
                 fg='#666', font=('Arial', 9)).pack(anchor='w')
        tk.Button(f1, text='  Ouvrir app.netlify.com →  ', bg='#1a1a1a',
                  fg='#d4af37', relief='flat', font=('Arial', 9, 'bold'),
                  cursor='hand2', padx=8, pady=5,
                  command=lambda: webbrowser.open(
                      'https://app.netlify.com/user/applications/personal')
                  ).pack(anchor='w', pady=6)
        tk.Label(f1, text='User settings → Applications → Personal access tokens → New token',
                 bg='#0a0a0a', fg='#2a2a2a', font=('Arial', 8)).pack(anchor='w')

        tk.Frame(self, bg='#1a1a1a', height=1).pack(fill='x', pady=10, padx=24)

        # Step 2 — paste token
        f2 = tk.Frame(self, bg='#0a0a0a', padx=24)
        f2.pack(fill='x')
        tk.Label(f2, text='② Colle ton token ici :', bg='#0a0a0a',
                 fg='#666', font=('Arial', 9)).pack(anchor='w', pady=(0, 5))
        self.tok = tk.StringVar()
        tk.Entry(f2, textvariable=self.tok, bg='#111', fg='#d4af37',
                 insertbackground='#d4af37', font=('Courier', 10),
                 relief='flat', bd=0, highlightthickness=1,
                 highlightbackground='#2a2a2a', highlightcolor='#d4af37',
                 width=52).pack()

        tk.Frame(self, bg='#1a1a1a', height=1).pack(fill='x', pady=10, padx=24)

        # Deploy button
        self.btn = tk.Button(self, text='③  DÉPLOYER  →',
                             bg='#d4af37', fg='#000',
                             font=('Arial', 11, 'bold'), relief='flat',
                             cursor='hand2', padx=20, pady=9,
                             command=self._start)
        self.btn.pack()

        self.status = tk.StringVar(value='Prêt.')
        tk.Label(self, textvariable=self.status, bg='#0a0a0a',
                 fg='#444', font=('Arial', 9)).pack(pady=5)
        self.bar = ttk.Progressbar(self, mode='indeterminate', length=440)
        self.bar.pack()

    def _start(self):
        token = self.tok.get().strip()
        if not token.startswith('nfp_'):
            messagebox.showwarning('Token invalide',
                'Le token doit commencer par nfp_\nGénère-le sur app.netlify.com')
            return
        self.btn.config(state='disabled', text='En cours…')
        self.bar.start(12)
        threading.Thread(target=self._deploy, args=(token,), daemon=True).start()

    def _deploy(self, token):
        try:
            self._s('Construction du ZIP…')
            data, n = build_zip()
            self._s(f'Envoi vers Netlify ({len(data)/1024/1024:.1f} MB, {n} fichiers)…')
            url = f'https://api.netlify.com/api/v1/sites/{SITE_ID}/deploys'
            req = urllib.request.Request(url, data=data, method='POST',
                headers={'Authorization': f'Bearer {token}',
                         'Content-Type': 'application/zip'})
            with urllib.request.urlopen(req, timeout=300) as r:
                body = json.loads(r.read().decode())
            did   = body.get('id', '?')
            state = body.get('state', '?')
            self._s(f'✓ Déployé ! ID: {did[:12]}… · État: {state}')
            self.bar.stop()
            self.btn.config(text='✓ EN LIGNE !', bg='#2a6b2a', fg='#fff')
            messagebox.showinfo('Déploiement réussi !',
                f'✓ Site mis en ligne !\n\nDeploy ID : {did}\nÉtat      : {state}\n\n'
                f'Visible dans 1–2 min sur :\n{SITE_URL}')
            webbrowser.open(SITE_URL)
        except urllib.error.HTTPError as e:
            err = e.read().decode()[:200]
            self.bar.stop()
            self.btn.config(state='normal', text='③  DÉPLOYER  →', bg='#d4af37', fg='#000')
            self._s(f'Erreur HTTP {e.code}')
            messagebox.showerror('Erreur', f'HTTP {e.code}\n{err}\n\nToken expiré ? Génères-en un nouveau.')
        except Exception as e:
            self.bar.stop()
            self.btn.config(state='normal', text='③  DÉPLOYER  →', bg='#d4af37', fg='#000')
            self._s(f'Erreur : {e}')
            messagebox.showerror('Erreur', str(e))

    def _s(self, msg):
        self.after(0, lambda: self.status.set(msg))


if __name__ == '__main__':
    App().mainloop()
