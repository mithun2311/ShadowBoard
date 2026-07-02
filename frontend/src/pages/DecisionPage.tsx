import { useLocation, useNavigate } from "react-router-dom";
import {
  BrainCircuit,
  ArrowLeft,
} from "lucide-react";

export default function DecisionPage() {
  const navigate = useNavigate();
  const location = useLocation();

  const { question, response } = location.state || {};

  if (!question || !response) {
    return (
      <div className="min-h-screen flex items-center justify-center bg-slate-100">
        <div className="bg-white p-8 rounded-2xl shadow-md text-center">
          <h2 className="text-2xl font-semibold mb-3">
            No Result Found
          </h2>

          <p className="text-slate-500 mb-6">
            Please submit a query from the dashboard.
          </p>

          <button
            onClick={() => navigate("/dashboard")}
            className="bg-slate-900 text-white px-5 py-3 rounded-lg hover:bg-slate-800"
          >
            Back to Dashboard
          </button>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-slate-100">

      <header className="bg-white border-b border-slate-200">
        <div className="max-w-5xl mx-auto px-6 py-6">

          <button
            onClick={() => navigate("/dashboard")}
            className="flex items-center gap-2 text-slate-600 hover:text-slate-900"
          >
            <ArrowLeft size={18} />
            Back
          </button>

          <div className="flex items-center gap-3 mt-6">

            <BrainCircuit
              size={34}
              className="text-indigo-600"
            />

            <div>
              <h1 className="text-3xl font-bold text-slate-900">
                AI Recommendation
              </h1>

              <p className="text-slate-500">
                ShadowBoard Executive Analysis
              </p>
            </div>

          </div>

        </div>
      </header>

      <main className="max-w-5xl mx-auto p-6 space-y-6">

        <section className="bg-white rounded-2xl shadow-sm border border-slate-200 p-6">

          <h2 className="text-lg font-semibold mb-3">
            Your Question
          </h2>

          <p className="text-slate-700 leading-7">
            {question}
          </p>

        </section>

        <section className="bg-white rounded-2xl shadow-sm border border-slate-200 p-6">

          <h2 className="text-lg font-semibold mb-4">
            AI Response
          </h2>

          <div className="whitespace-pre-wrap leading-8 text-slate-700">
            {response}
          </div>

        </section>

      </main>

    </div>
  );
}