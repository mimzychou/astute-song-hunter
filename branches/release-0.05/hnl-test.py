import line
import tkSnack, Tkinter

def HNL(c):
    (UP,DOWN,NUTRAL) = ('H','L','N')
    APPROX = 5
    i = 0
    while c[i] == 0:
      i += 1
    c = c[i:]
    x = UP
    i = 1
    while i < len(c):
      v = c[i] - c[i-1]
      if abs(v) <= APPROX:
        x += NUTRAL
      elif v < 0 :
        x += DOWN
      else:
        x += UP
      i += 1
    return x

def main():
    root = Tkinter.Tk()
    tkSnack.initializeSnack(root)
    Snd1 = tkSnack.Sound(load="songs/Roja.wav")
    Snd2 = tkSnack.Sound(load="tunes/nin_2.wav")
    Y1 = Snd1.dBPowerSpectrum(fftlength=16384)
    Ang1 = line.normalize(Y1)
    
    Y2 = Snd2.dBPowerSpectrum(fftlength=16384)
    Ang2 = line.normalize(Y2)
    print line.angle(Ang1, Ang2)


if __name__ == "__main__":
    main()
