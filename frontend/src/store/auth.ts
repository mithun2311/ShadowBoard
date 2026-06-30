import { create } from "zustand";

interface AuthState {
  token: string | null;
  setToken: (token: string) => void;
  logout: () => void;
}

export const useAuth = create<AuthState>((set) => ({
  token: localStorage.getItem("shadowboard_token"),

  setToken: (token: string) => {
    localStorage.setItem("shadowboard_token", token);
    set({ token });
  },

  logout: () => {
    localStorage.removeItem("shadowboard_token");
    set({ token: null });
  },
}));