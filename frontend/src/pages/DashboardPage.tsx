import { useState } from "react";
import { useNavigate } from "react-router-dom";
import {
  useMutation,
} from "@tanstack/react-query";
import {
  Upload,
  BrainCircuit,
  LogOut,
} from "lucide-react";
import { useEffect } from "react";
import { api } from "../lib/api";
import { useAuth } from "../store/auth";

export default function DashboardPage() {
const projectId =
  localStorage.getItem("current_project_id") || "";

  const [file, setFile] = useState<File | null>(null);
  const [question, setQuestion] = useState("");

  const navigate = useNavigate();
  useEffect(() => {
  if (!projectId) {
    navigate("/projects/new");
  }
}, [projectId, navigate]);
  const logout = useAuth((state) => state.logout);


const handleLogout = () => {
  localStorage.removeItem("current_project_id");
  logout();
  navigate("/");
};

const uploadMutation = useMutation({
  mutationFn: async () => {
    if (!projectId) {
  throw new Error("No project selected.");
}
    const formData = new FormData();

    formData.append("file", file as File);

    return api.post(
      `/documents/upload/${projectId}`,
      formData,
      {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      }
    );
  },

  onSuccess: () => {
    alert("Document uploaded successfully.");
    setFile(null);
  },

  onError: () => {
    alert("Failed to upload document.");
  },
});

const decisionMutation = useMutation({
  mutationFn: async () => {
    if (!projectId) {
      throw new Error("No project selected.");
    }

    return api.post("/ai/query", {
      query: question,
    });
  },

  onSuccess: (response) => {
    navigate("/decisions/result", {
      state: {
        question,
        response: response.data.response,
      },
    });
  },

  onError: () => {
    alert("Unable to generate a response. Please try again.");
  },
});

  return (
    <div className="min-h-screen bg-slate-100">

      {/* Navbar */}

      <header className="bg-white border-b border-slate-200">
        <div className="max-w-7xl mx-auto px-6 py-4 flex justify-between items-center">

          <div>
            <h1 className="text-2xl font-bold text-slate-900">
              ShadowBoard AI
            </h1>

            <p className="text-sm text-slate-500">
              Executive Decision Dashboard
            </p>
          </div>

<div className="flex items-center gap-3">
  <button
    onClick={() => navigate("/projects/new")}
    className="bg-indigo-600 text-white px-4 py-2 rounded-lg hover:bg-indigo-700"
  >
    New Project
  </button>

  <button
    onClick={handleLogout}
    className="flex items-center gap-2 bg-slate-900 text-white px-4 py-2 rounded-lg hover:bg-slate-800"
  >
    <LogOut size={18} />
    Logout
  </button>
</div>

        </div>
      </header>

      <main className="max-w-7xl mx-auto p-6">

        <div className="grid lg:grid-cols-2 gap-6">

          {/* Upload Card */}

          <section className="bg-white rounded-2xl shadow-sm border border-slate-200 p-6">

            <div className="flex items-center gap-3 mb-6">
              <Upload className="text-indigo-600" />
              <h2 className="text-xl font-semibold">
                Upload Documents
              </h2>
            </div>

<label
  htmlFor="file-upload"
  className="flex flex-col items-center justify-center
             w-full h-48
             border-2 border-dashed border-slate-300
             rounded-xl
             cursor-pointer
             hover:border-indigo-500
             hover:bg-slate-50
             transition"
>
  <Upload
    size={36}
    className="text-indigo-600 mb-3"
  />

  <p className="font-medium text-slate-700">
    Click to browse
  </p>

  <p className="text-sm text-slate-500 mt-1">
    PDF, DOCX or TXT
  </p>

  {file && (
    <p className="mt-4 text-sm font-medium text-indigo-600">
      {file.name}
    </p>
  )}

  <input
    id="file-upload"
    type="file"
    className="hidden"
    onChange={(e) =>
      setFile(e.target.files?.[0] || null)
    }
  />
</label>

            <button
              onClick={() => uploadMutation.mutate()}
              disabled={!file || uploadMutation.isPending}
              className="mt-5 w-full bg-indigo-600 hover:bg-indigo-700 text-white rounded-lg py-3 transition disabled:opacity-50"
            >
              {uploadMutation.isPending
                ? "Uploading..."
                : "Upload Document"}
            </button>

            <div className="mt-8">

  <p className="text-slate-500 text-sm">
    Upload a document before asking ShadowBoard AI.
    Uploaded files are stored securely for this project.
  </p>
</div>

          </section>

          {/* Decision Card */}

          <section className="bg-white rounded-2xl shadow-sm border border-slate-200 p-6">

            <div className="flex items-center gap-3 mb-6">
              <BrainCircuit className="text-indigo-600" />
              <h2 className="text-xl font-semibold">
                Strategic Decision
              </h2>
            </div>

            <textarea
              rows={8}
              value={question}
              onChange={(e) => setQuestion(e.target.value)}
              placeholder="Describe the strategic decision you want the AI board to evaluate..."
              className="w-full rounded-lg border border-slate-300 p-4 resize-none focus:ring-2 focus:ring-indigo-300 outline-none"
            />

            <button
              disabled={
                !question ||
                decisionMutation.isPending
              }
              onClick={() => decisionMutation.mutate()}
              className="mt-5 w-full bg-slate-900 hover:bg-slate-800 text-white rounded-lg py-3 transition disabled:opacity-50"
            >
              {decisionMutation.isPending
                ? "Generating..."
                : "Ask ShadowBoard AI"}
            </button>
          </section>

        </div>

      </main>

    </div>
  );
}