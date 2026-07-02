import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import { api } from "../lib/api";

export default function SignupPage() {
  const navigate = useNavigate();

  const [fullName, setFullName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");

  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const [success, setSuccess] = useState("");

  const submit = async (e: React.FormEvent) => {
    e.preventDefault();

    setError("");
    setSuccess("");

    if (password !== confirmPassword) {
      setError("Passwords do not match.");
      return;
    }

    try {
      setLoading(true);

      // Replace the endpoint below with the actual backend endpoint
      await api.post("/auth/register", {
        full_name: fullName,
        email,
        password,
      });

      setSuccess("Account created successfully! Redirecting to login...");

      setTimeout(() => {
        navigate("/");
      }, 1500);
    } catch (err: any) {
      setError(
  err.response?.data?.detail ||
  err.response?.data?.message ||
  "Registration failed. Please try again."
);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-slate-100 flex">

      {/* Left Panel */}

      <div className="hidden lg:flex w-1/2 bg-slate-900 text-white flex-col justify-center px-20">

        <p className="uppercase tracking-[0.3em] text-sm text-slate-400 mb-6">
          ShadowBoard AI
        </p>

        <h1 className="text-5xl font-bold leading-tight">
          Build Smarter
          <br />
          Decisions Together
        </h1>

        <p className="mt-8 text-lg text-slate-300 leading-8 max-w-lg">
          Create an account to start collaborating with AI agents,
          upload documents, and receive executive-level recommendations.
        </p>

      </div>

      {/* Signup Card */}

      <div className="flex-1 flex items-center justify-center p-8">

        <form
          onSubmit={submit}
          className="w-full max-w-md bg-white rounded-2xl shadow-lg p-10"
        >

          <h2 className="text-3xl font-bold text-slate-800">
            Create Account
          </h2>

          <p className="text-slate-500 mt-2 mb-8">
            Join ShadowBoard AI.
          </p>

          {error && (
            <div className="mb-5 rounded-lg bg-red-50 border border-red-200 p-3 text-red-600 text-sm">
              {error}
            </div>
          )}

          {success && (
            <div className="mb-5 rounded-lg bg-green-50 border border-green-200 p-3 text-green-700 text-sm">
              {success}
            </div>
          )}

          <div className="space-y-5">

            <div>

              <label className="block text-sm font-medium text-slate-700 mb-2">
                Full Name
              </label>

              <input
                type="text"
                placeholder="John Doe"
                value={fullName}
                onChange={(e) => setFullName(e.target.value)}
                required
                className="w-full rounded-lg border border-slate-300 px-4 py-3 outline-none focus:border-indigo-500 focus:ring-2 focus:ring-indigo-200"
              />

            </div>

            <div>

              <label className="block text-sm font-medium text-slate-700 mb-2">
                Email
              </label>

              <input
                type="email"
                placeholder="john@example.com"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                required
                className="w-full rounded-lg border border-slate-300 px-4 py-3 outline-none focus:border-indigo-500 focus:ring-2 focus:ring-indigo-200"
              />

            </div>

            <div>

              <label className="block text-sm font-medium text-slate-700 mb-2">
                Password
              </label>

              <input
                type="password"
                placeholder="••••••••"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                required
                className="w-full rounded-lg border border-slate-300 px-4 py-3 outline-none focus:border-indigo-500 focus:ring-2 focus:ring-indigo-200"
              />

            </div>

            <div>

              <label className="block text-sm font-medium text-slate-700 mb-2">
                Confirm Password
              </label>

              <input
                type="password"
                placeholder="••••••••"
                value={confirmPassword}
                onChange={(e) => setConfirmPassword(e.target.value)}
                required
                className="w-full rounded-lg border border-slate-300 px-4 py-3 outline-none focus:border-indigo-500 focus:ring-2 focus:ring-indigo-200"
              />

            </div>

            <button
              type="submit"
              disabled={loading}
              className="w-full rounded-lg bg-slate-900 py-3 text-white font-medium transition hover:bg-slate-800 disabled:opacity-50"
            >
              {loading ? "Creating Account..." : "Create Account"}
            </button>

            <div className="text-center text-sm text-slate-600">
              Already have an account?{" "}
              <Link
                to="/"
                className="font-medium text-indigo-600 hover:underline"
              >
                Sign In
              </Link>
            </div>

          </div>

          <p className="mt-8 text-center text-sm text-slate-400">
            ShadowBoard AI • Multi-Agent Executive Decision Platform
          </p>

        </form>

      </div>

    </div>
  );
}