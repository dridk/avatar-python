# generated by datamodel-codegen:
#   filename:  <stdin>
#   timestamp: 2022-06-07T13:38:28+00:00

from __future__ import annotations

from enum import Enum
from typing import Dict, List, Optional, Union
from uuid import UUID

from pydantic import BaseModel, Field, constr


class AnalysisStatus(Enum):
    started = "started"
    done = "done"


class ColumnType(Enum):
    int = "int"
    bool = "bool"
    category = "category"
    float = "float"


class ExplainedVariance(BaseModel):
    raw: List[float] = Field(..., title="Raw")
    ratio: List[float] = Field(..., title="Ratio")


class JobParameters(BaseModel):
    k: int = Field(..., title="K")
    column_weights: Optional[Dict[str, float]] = Field(None, title="Column Weights")
    ncp: Optional[int] = Field(None, title="Ncp")
    k_impute: Optional[int] = Field(None, title="K Impute")
    seed: Optional[int] = Field(None, title="Seed")


class JobStatus(Enum):
    pending = "pending"
    started = "started"
    success = "success"
    failure = "failure"
    unknown = "unknown"


class LoginResponse(BaseModel):
    access_token: str = Field(..., title="Access Token")
    token_type: str = Field(..., title="Token Type")


class Projections(BaseModel):
    records: List[List[float]] = Field(..., title="Records")
    avatars: List[List[float]] = Field(..., title="Avatars")


class SecurityMetrics(BaseModel):
    hidden_rate: float = Field(..., title="Hidden Rate")
    local_cloaking: float = Field(..., title="Local Cloaking")


class UserRole(Enum):
    admin = "admin"
    user = "user"


class ValidationError(BaseModel):
    loc: List[Union[str, int]] = Field(..., title="Location")
    msg: str = Field(..., title="Message")
    type: str = Field(..., title="Error Type")


class Login(BaseModel):
    grant_type: Optional[constr(regex=r"password")] = Field(None, title="Grant Type")
    username: str = Field(..., title="Username")
    password: str = Field(..., title="Password")
    scope: Optional[str] = Field("", title="Scope")
    client_id: Optional[str] = Field(None, title="Client Id")
    client_secret: Optional[str] = Field(None, title="Client Secret")


class CreateDataset(BaseModel):
    file: bytes = Field(..., title="File")


class ColumnDetail(BaseModel):
    type: ColumnType
    label: str = Field(..., title="Label")


class CreateUser(BaseModel):
    username: str = Field(..., title="Username")
    role: Optional[UserRole] = "user"
    password: constr(min_length=12) = Field(..., title="Password")


class DatasetResponse(BaseModel):
    id: UUID = Field(..., title="Id")
    hash: str = Field(..., title="Hash")
    name: Optional[str] = Field(None, title="Name")
    columns: Optional[List[ColumnDetail]] = Field(None, title="Columns")
    download_url: str = Field(..., title="Download Url")
    analysis_status: Optional[AnalysisStatus] = None
    analysis_duration: Optional[float] = Field(None, title="Analysis Duration")
    nb_lines: Optional[int] = Field(None, title="Nb Lines")


class HTTPValidationError(BaseModel):
    detail: Optional[List[ValidationError]] = Field(None, title="Detail")


class JobCreate(BaseModel):
    dataset_id: UUID = Field(..., title="Dataset Id")
    parameters: JobParameters


class PatchDataset(BaseModel):
    columns: List[ColumnDetail] = Field(..., title="Columns")


class AvatarizationResultResponse(BaseModel):
    metrics: SecurityMetrics
    avatars_dataset: DatasetResponse


class JobResponse(BaseModel):
    id: UUID = Field(..., title="Id")
    status: JobStatus
    dataset_id: UUID = Field(..., title="Dataset Id")
    result: Optional[AvatarizationResultResponse] = None
