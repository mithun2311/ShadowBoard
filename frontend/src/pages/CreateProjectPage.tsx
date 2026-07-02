import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { api } from "../lib/api";

export default function CreateProjectPage() {
  const navigate = useNavigate();

  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");
  const [industry, setIndustry] = useState("");
  const [companyStage, setCompanyStage] = useState("");
  const [decisionType, setDecisionType] = useState("");

  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const submit = async (e: React.FormEvent) => {
    e.preventDefault();

    setError("");

    try {
      setLoading(true);

      const response = await api.post("/projects", {
        title,
        description,
        industry,
        company_stage: companyStage,
        decision_type: decisionType,
      });

      localStorage.setItem(
        "current_project_id",
        response.data.id
      );

      navigate("/dashboard");
    } catch (err: any) {
      setError(
        err.response?.data?.detail ??
          "Unable to create project."
      );
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-slate-100 flex items-center justify-center p-6">

      <form
        onSubmit={submit}
        className="bg-white rounded-2xl shadow-lg p-10 w-full max-w-2xl"
      >
        <h1 className="text-3xl font-bold text-slate-900">
          Create Your Project
        </h1>

        <p className="text-slate-500 mt-2 mb-8">
          Set up a project before using ShadowBoard AI.
        </p>

        {error && (
          <div className="mb-5 rounded-lg bg-red-50 border border-red-200 p-3 text-red-600">
            {error}
          </div>
        )}

        <div className="space-y-5">

          <input
            placeholder="Project Title"
            value={title}
            onChange={(e) => setTitle(e.target.value)}
            required
            className="w-full rounded-lg border border-slate-300 p-3"
          />

          <textarea
            placeholder="Project Description"
            rows={4}
            value={description}
            onChange={(e) => setDescription(e.target.value)}
            required
            className="w-full rounded-lg border border-slate-300 p-3"
          />

          <input
            placeholder="Industry"
            value={industry}
            onChange={(e) => setIndustry(e.target.value)}
            required
            className="w-full rounded-lg border border-slate-300 p-3"
          />

          <input
            placeholder="Company Stage"
            value={companyStage}
            onChange={(e) => setCompanyStage(e.target.value)}
            required
            className="w-full rounded-lg border border-slate-300 p-3"
          />

          <input
            placeholder="Decision Type"
            value={decisionType}
            onChange={(e) => setDecisionType(e.target.value)}
            required
            className="w-full rounded-lg border border-slate-300 p-3"
          />

          <button
            disabled={loading}
            className="w-full bg-slate-900 text-white rounded-lg py-3 hover:bg-slate-800 disabled:opacity-50"
          >
            {loading ? "Creating..." : "Create Project"}
          </button>

        </div>
      </form>

    </div>
  );
}