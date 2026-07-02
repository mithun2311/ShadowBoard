import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import { api } from "../lib/api";
import { useAuth } from "../store/auth";

export default function LoginPage() {
  const navigate = useNavigate();

  const setToken = useAuth((state) => state.setToken);

  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const submit = async (e: React.FormEvent) => {
    e.preventDefault();

    setError("");

    try {
      setLoading(true);

      const formData = new URLSearchParams();

      formData.append("username", email);
      formData.append("password", password);

      // Login
      const response = await api.post(
        "/auth/login",
        formData,
        {
          headers: {
            "Content-Type":
              "application/x-www-form-urlencoded",
          },
        }
      );

      const token = response.data.access_token;

      // Save JWT
      setToken(token);

      // Ensure Axios interceptor has access immediately
      localStorage.setItem("shadowboard_token", token);

      // Fetch user's projects
      const projectsResponse = await api.get("/projects");

      const projects = projectsResponse.data;

      if (projects.length > 0) {
        // Save first project
        localStorage.setItem(
          "current_project_id",
          projects[0].id
        );

        navigate("/dashboard");
      } else {
        // First login → create project
        navigate("/create-project");
      }
    } catch (err: any) {
      setError(
        err.response?.data?.detail ||
          "Invalid email or password."
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
          Executive Intelligence
          <br />
          for Better Decisions
        </h1>

        <p className="mt-8 text-lg text-slate-300 leading-8 max-w-lg">
          ShadowBoard AI helps leadership teams evaluate
          strategic decisions through collaborative AI
          agents, document analysis, and risk-aware
          recommendations.
        </p>

      </div>

      {/* Login Card */}

      <div className="flex-1 flex items-center justify-center p-8">

        <form
          onSubmit={submit}
          className="w-full max-w-md bg-white rounded-2xl shadow-lg p-10"
        >

          <h2 className="text-3xl font-bold text-slate-800">
            Welcome Back
          </h2>

          <p className="text-slate-500 mt-2 mb-8">
            Sign in to continue to ShadowBoard AI.
          </p>

          {error && (
            <div className="mb-5 rounded-lg bg-red-50 border border-red-200 p-3 text-red-600 text-sm">
              {error}
            </div>
          )}

          <div className="space-y-6">

            <div>

              <label className="block text-sm font-medium text-slate-700 mb-2">
                Email
              </label>

              <input
                type="email"
                placeholder="john@example.com"
                value={email}
                onChange={(e) =>
                  setEmail(e.target.value)
                }
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
                onChange={(e) =>
                  setPassword(e.target.value)
                }
                required
                className="w-full rounded-lg border border-slate-300 px-4 py-3 outline-none focus:border-indigo-500 focus:ring-2 focus:ring-indigo-200"
              />

            </div>

            <button
              type="submit"
              disabled={loading}
              className="w-full rounded-lg bg-slate-900 py-3 text-white font-medium transition hover:bg-slate-800 disabled:opacity-50"
            >
              {loading ? "Signing In..." : "Sign In"}
            </button>

            <div className="text-center text-sm text-slate-600">
              Don't have an account?{" "}
              <Link
                to="/signup"
                className="font-medium text-indigo-600 hover:underline"
              >
                Create an Account
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