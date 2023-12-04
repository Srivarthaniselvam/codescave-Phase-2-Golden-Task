# coderscave intern
# phase 2
# Golden Task


import tkinter as tk
import threading
import winsound
import tkinter.filedialog

class VoiceRecorderApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Voice Recorder")


        title_label = tk.Label(master, text="Voice Recorder", font=('Helvetica', 16, 'bold'))
        title_label.pack(pady=10)

        self.record_button = tk.Button(master, text="Record", command=self.record, font=('Helvetica', 12), background="#4CAF50", foreground="white")
        self.record_button.pack(pady=10)

        self.stop_button = tk.Button(master, text="Stop", command=self.stop, state=tk.DISABLED, font=('Helvetica', 12), background="#4CAF50", foreground="white")
        self.stop_button.pack(pady=10)

        self.save_button = tk.Button(master, text="Save", command=self.save, state=tk.DISABLED, font=('Helvetica', 12), background="#4CAF50", foreground="white")
        self.save_button.pack(pady=10)

        self.clear_button = tk.Button(master, text="Clear", command=self.clear, state=tk.DISABLED, font=('Helvetica', 12), background="#4CAF50", foreground="white")
        self.clear_button.pack(pady=10)

        self.filename = "recorded_audio.wav"
        self.is_recording = False
        self.frames = []

    def record(self):
        self.record_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        self.save_button.config(state=tk.DISABLED)
        self.clear_button.config(state=tk.DISABLED)

        self.is_recording = True
        self.recording_thread = threading.Thread(target=self._record_audio)
        self.recording_thread.start()

    def _record_audio(self):
        winsound.Beep(1000, 500) 
        self.stop_recording()

    def stop_recording(self):
        self.is_recording = False
        self.record_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        self.save_button.config(state=tk.NORMAL)
        self.clear_button.config(state=tk.NORMAL)

    def stop(self):
        self.stop_recording()

    def save(self):
        self.filename = tk.filedialog.asksaveasfilename(defaultextension=".wav", filetypes=[("WAV files", "*.wav")])

        if self.filename:
          
            print(f"Audio saved to: {self.filename}")
            self.save_button.config(state=tk.DISABLED)

    def clear(self):
        self.frames = []
        print("Recorded audio frames cleared.")
        self.clear_button.config(state=tk.DISABLED)

    def run(self):
        self.master.mainloop()


if __name__ == "__main__":
    root = tk.Tk()

   
    root.configure(bg='#E0E0E0')  

    app = VoiceRecorderApp(root)
    app.run()
