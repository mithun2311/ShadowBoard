import { useState } from "react";
import { useNavigate } from "react-router-dom";
import {
  useQuery,
  useMutation,
  useQueryClient,
} from "@tanstack/react-query";
import {
  Upload,
  FileText,
  BrainCircuit,
  LogOut,
} from "lucide-react";

import { api } from "../lib/api";
import { useAuth } from "../store/auth";
import type { DocumentItem } from "../types";

export default function DashboardPage() {
  const [projectId] = useState(
    localStorage.getItem("current_project_id") || ""
  );

  const [file, setFile] = useState<File | null>(null);
  const [question, setQuestion] = useState("");

  const navigate = useNavigate();
  const logout = useAuth((state) => state.logout);

  const queryClient = useQueryClient();

  const handleLogout = () => {
    logout();
    navigate("/");
  };

  const { data: documents } = useQuery<DocumentItem[]>({
    queryKey: ["documents", projectId],
    queryFn: async () =>
      (await api.get(`/api/v1/projects/${projectId}/documents`)).data,
    enabled: !!projectId,
  });

  const uploadMutation = useMutation({
    mutationFn: async () => {
      const formData = new FormData();

      formData.append("project_id", projectId);
      formData.append("file", file as File);

      return api.post("/api/v1/documents/upload", formData, {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      });
    },

    onSuccess: () =>
      queryClient.invalidateQueries({
        queryKey: ["documents", projectId],
      }),
  });

  const decisionMutation = useMutation({
    mutationFn: async () =>
      api.post("/api/v1/decisions/", {
        project_id: projectId,
        question,
      }),
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

          <button
            onClick={handleLogout}
            className="flex items-center gap-2 bg-slate-900 text-white px-4 py-2 rounded-lg hover:bg-slate-800 transition"
          >
            <LogOut size={18} />
            Logout
          </button>

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

              <h3 className="font-medium mb-3">
                Uploaded Files
              </h3>

              <div className="space-y-3">

                {documents?.length ? (
                  documents.map((doc) => (
                    <div
                      key={doc.id}
                      className="flex justify-between items-center border rounded-lg p-3"
                    >
                      <div className="flex items-center gap-3">

                        <FileText
                          size={18}
                          className="text-slate-500"
                        />

                        <div>

                          <p className="font-medium">
                            {doc.filename}
                          </p>

                          <p className="text-xs text-slate-500">
                            {doc.chunk_count} chunks
                          </p>

                        </div>

                      </div>

                      <span className="text-xs bg-slate-100 px-2 py-1 rounded">
                        {doc.status}
                      </span>

                    </div>
                  ))
                ) : (
                  <p className="text-slate-500 text-sm">
                    No documents uploaded.
                  </p>
                )}

              </div>

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
                ? "Submitting..."
                : "Convene the Board"}
            </button>

            {decisionMutation.data && (
              <a
                href={`/decisions/${decisionMutation.data.data.id}`}
                className="block mt-5 text-indigo-600 hover:underline font-medium"
              >
                View Live Decision →
              </a>
            )}

          </section>

        </div>

      </main>

    </div>
  );
}